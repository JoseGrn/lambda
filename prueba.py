import json

def lambda_handler(event, context):
    # TODO implement
    data = json.dumps({"carros":["BMW","TOYOTA", "MAZDA"],
            "mensaje":"hola desde una funcion muy bonita"
            })
    return {
        'statusCode': 200,
        'body': data
    }