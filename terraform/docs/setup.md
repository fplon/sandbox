## Setting up GitHub Actions Permissions

```bash
gcloud iam service-accounts create [SA_NAME] \
    --description="Service account for GitHub Actions" \
    --display-name="GitHub Actions SA"
```

```bash
gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/storage.admin"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/storage.objectViewer"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/storage.objectCreator"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/storage.objectAdmin"
```

```bash
gcloud iam service-accounts keys create key.json \
    --iam-account=[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com
```

```bash
gh secret set GOOGLE_CREDENTIALS < key.json
```

```bash
rm key.json
```


## Setting up backend state storage

Create a new bucket for Terraform state
```bash
gcloud storage buckets create [STATE_BUCKET] \
    --location=[REGION] \
    --uniform-bucket-level-access
```

Add versioning to protect state history
```bash
gcloud storage buckets update [STATE_BUCKET] \
    --versioning
```

## Rolling out a release on GH - to deploy production infra
Create and push a new tag
```bash
git tag v1.0.0
git push origin v1.0.0
```

Create a release from the tag
```bash
gh release create v1.0.0 --title "Version 1.0.0" --notes "Description of changes"
```
