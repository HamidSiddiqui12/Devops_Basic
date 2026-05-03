# Restaurant Bill Calculator

meal_cost = float(input("Enter the meal cost: "))

Service_Charge = meal_cost*0.10
Amount_After_Service = meal_cost + Service_Charge
Tax = Amount_After_Service*0.05
tip = Amount_After_Service*0.05
Total_Bill = Amount_After_Service + Tax + tip

print(f"""--- Receipt ---
Meal Cost: {meal_cost:.2f}
Service Charge (10%): {Service_Charge:.2f}
Amount After Service: {Amount_After_Service:.2f}
Tax (5%): {Tax:.2f}
Tip (5%): {tip:.2f}
Total Bill: {Total_Bill:.2f}
""")