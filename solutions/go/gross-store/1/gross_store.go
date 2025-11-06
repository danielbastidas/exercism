package gross

// Units stores the Gross Store unit measurements.
func Units() map[string]int {
	units := map[string]int{}

    units["quarter_of_a_dozen"] = 3
    units["half_of_a_dozen"] = 6
    units["dozen"] = 12
    units["small_gross"] = 120
    units["gross"] = 144
    units["great_gross"] = 1728

    return units
    
}

// NewBill creates a new bill.
func NewBill() map[string]int {
	return map[string]int{}
}

// AddItem adds an item to customer bill.
func AddItem(bill, units map[string]int, item, unit string) bool {
	amount, exists := units[unit]

    if exists {
    	quantity, alreadyBilled := bill[item]
        if alreadyBilled {
        	bill[item] = quantity + amount
        } else {
            bill[item] = amount
        }
        
    }

    return exists
}

// RemoveItem removes an item from customer bill.
func RemoveItem(bill, units map[string]int, item, unit string) bool {
	billQuantity, itemExists := bill[item]
	unitQuantity, unitExists := units[unit]
    response := true

    if !itemExists || !unitExists {
        response = false
    }

    newQuantity := billQuantity - unitQuantity

    if newQuantity < 0 {
        response  = false
    } else {
        bill[item] = newQuantity
    }

    if newQuantity == 0 {
        delete(bill, item)
        response = true
    }

    return response
}

// GetItem returns the quantity of an item that the customer has in his/her bill.
func GetItem(bill map[string]int, item string) (int, bool) {
	quantity, exists := bill[item]

    if !exists {
        return 0, false
    }

    return quantity, true
}
