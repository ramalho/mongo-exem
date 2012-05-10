
# Email each supplier of this product.
# Default value is the empty list so no special casing
# is needed if the suppliers property is not present.
for supplier in product_doc.get("suppliers", []):
    email_supplier(supplier)
