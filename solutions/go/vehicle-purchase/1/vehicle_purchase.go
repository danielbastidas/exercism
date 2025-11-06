package purchase

// NeedsLicense determines whether a license is needed to drive a type of vehicle. Only "car" and "truck" require a license.
func NeedsLicense(kind string) bool {
	return kind == "car" || kind == "truck"
}

// ChooseVehicle recommends a vehicle for selection. It always recommends the vehicle that comes first in lexicographical order.
func ChooseVehicle(option1, option2 string) string {

    var result string
    if option1 < option2 {
        result = option1
    } else {
        result = option2
    }

    return result + " is clearly the better choice."
}

// CalculateResellPrice calculates how much a vehicle can resell for at a certain age.
func CalculateResellPrice(originalPrice, age float64) float64 {

    var price float64
    if age < 3 {
        price = (80 * originalPrice) / 100
    } else if age >= 3 && age < 10 {
        price = (70 * originalPrice) / 100
    } else {
        price = (50 * originalPrice) / 100
    }

    return price
}
