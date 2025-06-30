variable "project_id" {
  description = "The ID of the GCP project"
  type        = string
}
# blah

variable "environment" {
  description = "Environment (production or development)"
  type        = string
  validation {
    condition     = contains(["development", "production"], var.environment)
    error_message = "Environment must be either 'development' or 'production'"
  }
}

variable "region" {
  description = "The region to deploy resources to"
  type        = string
  default     = "europe-west2" # london
}

variable "bucket_versioning" {
  description = "Enable versioning for storage buckets"
  type        = bool
  default     = true
}

