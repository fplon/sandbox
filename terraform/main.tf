terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
  backend "gcs" {
    # Bucket name will be provided via backend config
  }
}


# Configure GCP Provider
provider "google" {
  project = var.project_id
  region  = var.region
}

# Create GCS buckets for medallion architecture
resource "google_storage_bucket" "bronze_layer" {
  name          = "${var.project_id}-${var.environment}-bronze"
  location      = var.region
  force_destroy = var.environment != "production"

  uniform_bucket_level_access = true
  versioning {
    enabled = true
  }

  labels = {
    environment = var.environment
    layer       = "bronze"
    managed_by  = "terraform"
  }

  lifecycle_rule {
    condition {
      age = var.environment == "production" ? 90 : 30
    }
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }
  }
}

resource "google_storage_bucket" "silver_layer" {
  name          = "${var.project_id}-${var.environment}-silver"
  location      = var.region
  force_destroy = var.environment != "production"

  uniform_bucket_level_access = true
  versioning {
    enabled = true
  }

  labels = {
    environment = var.environment
    layer       = "silver"
    managed_by  = "terraform"
  }
}

resource "google_storage_bucket" "gold_layer" {
  name          = "${var.project_id}-${var.environment}-gold"
  location      = var.region
  force_destroy = var.environment != "production"

  uniform_bucket_level_access = true
  versioning {
    enabled = true
  }

  labels = {
    environment = var.environment
    layer       = "gold"
    managed_by  = "terraform"
  }
}
