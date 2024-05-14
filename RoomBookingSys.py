def book_room(room_list):
    if not room_list:
        print("Sorry, all rooms have been booked!")
        return

    print("Available rooms:", room_list)
    room = input("Enter the room you want to book (example, 'Room 1'): ")

    if room not in room_list:
        print("Invalid room. Please choose from the available rooms in the list.")
        book_room(room_list)
        return

    client_name = input("Enter client's name: ")
    payment = input("Enter payment amount: ")

    print(line)
    print("Booking confirmed for " + client_name + " in " + room + " with payment of " + payment + ".")

    room_list.remove(room)

    another_booking = input("Do you want to book another room? (yes/no): ")
    if another_booking.lower() == 'yes':
        book_room(room_list)
    else:
        print(line)
        print("Thank you for your bookings!")
        print("Enjoy your stay!")

line = "--------------------------------------------------------------------"

print(line)
available_rooms = ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5']
book_room(available_rooms)
print(line)
