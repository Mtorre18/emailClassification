from transformers import pipeline

# Initialize the zero-shot classification pipeline
# This can be optimized by fine-tuning the model or training a custom model
classifier = pipeline("zero-shot-classification")

# Sample email - would want to start this when new emails is received
email = "There is a significant delay in the shipment of parts due to unexpected supply chain disruptions."

# Define actions for each category - unsure if these can be generated automatically
category_actions = {
    "Material Delay": ["Alert production", "Change PO due date in ERP system"],
    "Material Issue": ["Check for alternate parts", "Alert quality control", "Forward email to engineering"],
    "Material Obsolescence": ["Check for alternate parts", "Alert production", "Update BOM in ERP system"],
    "Material Change": ["Forward email to engineering", "Update BOM in ERP system", "Alert production"]
    # Add more categories and actions as needed
    # Tedious, not scalable, would like to generate these based on business type and software used (ERP, CAD, CRM, etc.)
}

custom_topics = ["Material Delay", "Material Issue", "Material Obsolescence", "Material Change"]

result = classifier(email, custom_topics)

# Find the top category
top_category = result["labels"][0]

# Suggest actions based on the top category
suggested_actions = category_actions.get(top_category, [])
print(f"\n {top_category}- Suggested Actions:")
for action in suggested_actions:
    print(f"- {action}")
