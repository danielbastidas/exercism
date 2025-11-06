package booking

import "time"
import "fmt"

func parseDate(date, format string) time.Time {
    t, err := time.Parse(format, date)

	if err != nil {
    	panic(err)
    }
    
    return t
}

// Schedule returns a time.Time from a string containing a date.
func Schedule(date string) time.Time {    
    layout := "1/02/2006 15:04:05"
    t := parseDate(date, layout)
    
    return t
}

// HasPassed returns whether a date has passed.
func HasPassed(date string) bool {
	layout := "January 2, 2006 15:04:05"
	t := parseDate(date, layout)
    
    return t.Before(time.Now())
}

// IsAfternoonAppointment returns whether a time is in the afternoon.
func IsAfternoonAppointment(date string) bool {
	layout := "Monday, January 2, 2006 15:04:05"
    appointment := parseDate(date, layout)

    return appointment.Hour() >= 12 && appointment.Hour() <= 18
}

// Description returns a formatted string of the appointment time.
func Description(date string) string {
	layout := "1/2/2006 15:04:05"
    appointment := parseDate(date, layout)

    return fmt.Sprintf("You have an appointment on %s, %s %d, %d, at %d:%d.", appointment.Weekday().String(), appointment.Month().String(), appointment.Day(), appointment.Year(), appointment.Hour(), appointment.Minute())
}

// AnniversaryDate returns a Time with this year's anniversary.
func AnniversaryDate() time.Time {
	currentYear := time.Now().Year()

    return time.Date(currentYear, time.September, 15, 00, 00, 00, 0, time.UTC)
}
