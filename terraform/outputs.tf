output "bronze_bucket_name" {
  value       = google_storage_bucket.bronze_layer.name
  description = "The name of the bronze bucket"
}

output "silver_bucket_name" {
  value       = google_storage_bucket.silver_layer.name
  description = "The name of the silver bucket"
}

output "gold_bucket_name" {
  value       = google_storage_bucket.gold_layer.name
  description = "The name of the gold bucket"
}

output "environment" {
  value       = var.environment
  description = "The environment where resources are deployed"
}
