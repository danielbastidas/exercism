// Package weather shows the weather conditions of a city.
package weather

// CurrentCondition represents the weather condition of a city. It holds a string value.
var CurrentCondition string
// CurrentLocation represents a city name. It's a string value.
var CurrentLocation string

// Forecast shows the weather conditions of a city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
