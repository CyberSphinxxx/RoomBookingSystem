def book_room(room_list):
    if not room_list:
        print("All rooms have been booked.")
        return

    print("Available rooms:", room_list)
    room = input("Enter the room you want to book (e.g., 'Room 101'): ")

    if room not in room_list:
        print("Invalid room. Please choose from the available rooms.")
        book_room(room_list)
        return

    client_name = input("Enter client's name: ")
    payment = input("Enter payment amount: ")

    print("Booking confirmed for " + client_name + " in " + room + " with payment of " + payment + ".")

    room_list.remove(room)

    another_booking = input("Do you want to book another room? (yes/no): ")
    if another_booking.lower() == 'yes':
        book_room(room_list)
    else:
        print("Thank you for your bookings!")

available_rooms = ['Room 101', 'Room 102', 'Room 103', 'Room 104']
book_room(available_rooms)
