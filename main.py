from pyscript import display, document


def SKU_generator(e):
  output_div = document.getElementById("sku_output")
  if output_div:
    output_div.innerHTML = ""
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("quantity").value

    if not product_name or not stock_qty:
      display("Please fill out all fields!", target="sku_output")
      return

    sku = (
        category[:3].upper()
        + "-"
        + product_name[:4].upper()
        + "-"
        + str(stock_qty)
    )
    display("SKU: " + sku, target="sku_output")


def create_order(e):
  try:
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    if not prod1:
      return

    subtotal = 0.0
    receipt = "<h4>==== Receipt ====</h4>"

    # List of items with their names and fixed prices
    items = [
        (prod1, "League of Legends Funko pops", 450.0),
        (prod2, "Gelato", 120.0),
        (prod3, "Dark Souls 3 (Deluxe)", 2499.0),
        (prod4, "Tiramisu (per slice)", 150.0),
        (prod5, "Jojo's Bizarre Adventure Part 7 (Vol)", 250.0),
    ]

    selected_count = 0
    for item, name, price in items:
      if item.checked:
        subtotal += price
        receipt += f"<p>{name}  ₱{price:.2f}</p>"
        selected_count += 1

    if selected_count == 0:
      receipt += "<p>No items selected.</p>"

    tax_rate = 0.12
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt += f"""
        <hr>
        <p>Subtotal: ₱{subtotal:.2f}</p>
        <p>VAT (12%): ₱{tax:.2f}</p>
        <p><strong>Total: ₱{total:.2f}</strong></p>
        """
    document.getElementById("show").innerHTML = receipt
  except Exception as err:
    document.getElementById("show").innerHTML = (
        f"<p style='color:red;'>Error: {err}</p>"
    )


try:
  gen_btn = document.getElementById("generate_btn")
  if gen_btn:
    gen_btn.addEventListener("click", SKU_generator)
except Exception:
  pass

try:
  order_btn = document.getElementById("order_btn")
  if order_btn:
    order_btn.addEventListener("click", create_order)
except Exception:
  pass
