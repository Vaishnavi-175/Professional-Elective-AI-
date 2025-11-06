def traffic_light_controller(traffic, pedestrian, emergency):
    if emergency:
        return "🔴 All Red - Let emergency vehicle pass"
    elif traffic == "high" and not pedestrian:
        return "🟢 Green Light - Heavy traffic, keep road open"
    elif pedestrian and traffic == "low":
        return "🔴 Red Light - Allow pedestrians to cross"
    elif traffic == "none":
        return "🔴 Red Light - No vehicles"
    else:
        return "🟡 Yellow Light - Prepare to stop"

print("=== Traffic Light Expert System ===\n")

traffic = input("Enter traffic level (high / low / none): ").strip().lower()
pedestrian_input = input("Is there a pedestrian waiting? (yes / no): ").strip().lower()
emergency_input = input("Is there an emergency vehicle? (yes / no): ").strip().lower()

pedestrian = pedestrian_input == "yes"
emergency = emergency_input == "yes"

decision = traffic_light_controller(traffic, pedestrian, emergency)

print("\n--- Decision ---")
print(decision)
print("\nThank you for using the Traffic Light Expert System!")
