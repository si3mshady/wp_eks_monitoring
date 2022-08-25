from unicodedata import name
import boto3, subprocess

HOSTED_ZONE_ID = 'Z03316531PQU1MAY9ZO09'
DOMAIN_NAME = 'elliottlamararnold.com'


r53 = boto3.client('route53',region_name='us-east-1')


def get_wordpress_alb_fqdn():
    cmd = "kubectl get svc | awk '/^wordpress/ {print $4}'"
    try: 
        output, _ = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()
        return str(output.decode().strip())
    except Exception as e:
        print(str(e))


def map_alb_to_domain(hosted_zone_id=HOSTED_ZONE_ID, domain_name=DOMAIN_NAME):
        r53.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
            "Comment": "Creating Alias resource record sets in Route 53",
            "Changes": [
                {
                "Action": "CREATE",
                "ResourceRecordSet": { "Name": f"blog.{domain_name}", "Type": "CNAME", 'TTL': 120,
                'ResourceRecords': [{'Value':  get_wordpress_alb_fqdn()},
                    ]
                }
                }
            ]
            }
        )


if __name__ == "__main__":
     map_alb_to_domain()



# https://stackoverflow.com/questions/46582196/invalidchangebatch-when-calling-the-changeresourcerecordsets-operation-using


# [Tried to create an alias that targets ae908cd290ff9448ab69f7fbdc517da5.,
#  type A in zone Z03316531PQU1MAY9ZO09, but the alias target name does not lie within the target zone,
#  Tried to create an alias that targets ae908cd290ff9448ab69f7fbdc517da5.,
#  type A in zone Z03316531PQU1MAY9ZO09, but that target was not found]
# Can only create an alias when you purchase domain via AWS. 
#With an alias you can associate a domain with pre-existing aws resources 