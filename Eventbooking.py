from tkinter import *
from tkinter import messagebox

class Event:
    def _init_(self, name, date, start_time, end_time):
        self.name = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time


class DetailCust:
    def _init_(self, contact_name, contact_email, number_phone):
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.number_phone = number_phone


class EventHallBookingSystem:
    def _init_(self):
        self.bookings = []

    def add_booking(self, event, detail_cust):
        self.bookings.append((event, detail_cust))
        messagebox.showinfo("Booking Success", "Booking added successfully!")

    def remove_booking(self, event):
        booking = self.find_booking(event)
        if booking:
            self.bookings.remove(booking)
            messagebox.showinfo("Booking Removal", "Booking removed successfully!")
        else:
            messagebox.showinfo("Booking Removal", "Booking not found.")

    def find_booking(self, event):
        for booking in self.bookings:
            if booking[0] == event:
                return booking
        return None

    def check_availability(self, date, start_time, end_time):
        for booking in self.bookings:
            event = booking[0]
            if event.date == date and (
                (start_time >= event.start_time and start_time < event.end_time)
                or (end_time > event.start_time and end_time <= event.end_time)
                or (start_time <= event.start_time and end_time >= event.end_time)
            ):
                return False
        return True

    def view_bookings(self):
        if len(self.bookings) == 0:
            messagebox.showinfo("View Bookings", "No bookings found.")
        else:
            bookings_info = "Existing bookings:\n\n"
            for index, booking in enumerate(self.bookings):
                event = booking[0]
                detail_cust = booking[1]
                bookings_info += f"{index + 1}. {event.name} - {event.date}, {event.start_time}-{event.end_time}\n"
                bookings_info += f"   Customer: {detail_cust.contact_name}, {detail_cust.contact_email}, {detail_cust.number_phone}\n\n"
            messagebox.showinfo("View Bookings", bookings_info)


def book_event():
    name = name_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    # Create objects
    detail_cust = DetailCust("", "", "")  # Empty values for contact details
    event = Event(name, date, time, time)  # Use the same time for start and end

    # Check availability and add the booking
    if not booking_system.check_availability(date, time, time):
        messagebox.showinfo("Booking Error", "The hall is already booked for that time.")
    else:
        booking_system.add_booking(event, detail_cust)

    # Clear the input fields
    name_entry.delete(0, END)
    date_entry.delete(0, END)
    time_entry.delete(0, END)


def remove_booking():
    booking_system.view_bookings()
    if len(booking_system.bookings) > 0:
        index = int(booking_number_entry.get())
        if index > 0 and index <= len(booking_system.bookings):
            event = booking_system.bookings[index - 1][0]
            booking_system.remove_booking(event)
        else:
            messagebox.showinfo("Invalid Booking Number", "Invalid booking number.")


def check_availability():
    date = check_date_entry.get()
    start_time = check_start_time_entry.get()
    end_time = check_end_time_entry.get()

    if booking_system.check_availability(date, start_time, end_time):
        messagebox.showinfo("Availability", "The hall is available for booking.")
    else:
        messagebox.showinfo("Availability", "The hall is already booked for that time.")


def view_bookings():
    booking_system.view_bookings()


booking_system = EventHallBookingSystem()

window = Tk()
window.title("Event Hall Booking System")

# Add Booking
add_booking_frame = LabelFrame(window, text="Add Booking")
add_booking_frame.pack(padx=10, pady=10)

name_label = Label(add_booking_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = Entry(add_booking_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

date_label = Label(add_booking_frame, text="Date:")
date_label.grid(row=1, column=0, padx=5, pady=5)
date_entry = Entry(add_booking_frame)
date_entry.grid(row=1, column=1, padx=5, pady=5)

time_label = Label(add_booking_frame, text="Time:")
time_label.grid(row=2, column=0, padx=5, pady=5)
time_entry = Entry(add_booking_frame)
time_entry.grid(row=2, column=1, padx=5, pady=5)

book_button = Button(add_booking_frame, text="Book Event", command=book_event)
book_button.grid(row=3, columnspan=2, padx=5, pady=5)


# Remove Booking
remove_booking_frame = LabelFrame(window, text="Remove Booking")
remove_booking_frame.pack(padx=10, pady=10)

booking_number_label = Label(remove_booking_frame, text="Booking Number:")
booking_number_label.grid(row=0, column=0, padx=5, pady=5)
booking_number_entry = Entry(remove_booking_frame)
booking_number_entry.grid(row=0, column=1, padx=5, pady=5)

remove_button = Button(remove_booking_frame, text="Remove Booking", command=remove_booking)
remove_button.grid(row=1, columnspan=2, padx=5, pady=5)


# Check Availability
check_availability_frame = LabelFrame(window, text="Check Availability")
check_availability_frame.pack(padx=10, pady=10)

check_date_label = Label(check_availability_frame, text="Date:")
check_date_label.grid(row=0, column=0, padx=5, pady=5)
check_date_entry = Entry(check_availability_frame)
check_date_entry.grid(row=0, column=1, padx=5, pady=5)

check_start_time_label = Label(check_availability_frame, text="Start Time:")
check_start_time_label.grid(row=1, column=0, padx=5, pady=5)
check_start_time_entry = Entry(check_availability_frame)
check_start_time_entry.grid(row=1, column=1, padx=5, pady=5)

check_end_time_label = Label(check_availability_frame, text="End Time:")
check_end_time_label.grid(row=2, column=0, padx=5, pady=5)
check_end_time_entry = Entry(check_availability_frame)
check_end_time_entry.grid(row=2, column=1, padx=5, pady=5)

check_button = Button(check_availability_frame, text="Check Availability", command=check_availability)
check_button.grid(row=3, columnspan=2, padx=5, pady=5)


# View Bookings
view_bookings_button = Button(window, text="View Bookings", command=view_bookings)
view_bookings_button.pack(padx=10, pady=10)


# Start the main loop
window.mainloop()