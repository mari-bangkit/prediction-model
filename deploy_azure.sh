ENDPOINT_NAME="maribangkit"

echo "Deleting previous endpoint with same name (if available)..."
az ml online-endpoint delete -n $ENDPOINT_NAME

echo -e "\nCreating online endpoint..."
az ml online-endpoint create -n $ENDPOINT_NAME -f manage/endpoint.yml

echo -e "\nCreating online deployment..."
az ml online-deployment create -n initial --endpoint $ENDPOINT_NAME -f manage/initial-deployment.yml --all-traffic

echo -e "\n-- FINAL STATUS --"
az ml online-endpoint show -n $ENDPOINT_NAME