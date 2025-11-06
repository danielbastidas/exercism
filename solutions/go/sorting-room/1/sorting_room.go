package sorting
import "fmt"
import "strconv"

// DescribeNumber should return a string describing the number.
func DescribeNumber(f float64) string {
	return fmt.Sprintf("This is the number %.1f", f)
}

type NumberBox interface {
	Number() int
}

// DescribeNumberBox should return a string describing the NumberBox.
func DescribeNumberBox(nb NumberBox) string {
	return fmt.Sprintf("This is a box containing the number %.1f", float64(nb.Number()))
}

type FancyNumber struct {
	n string
}

func (i FancyNumber) Value() string {
	return i.n
}

type FancyNumberBox interface {
	Value() string
}

// ExtractFancyNumber should return the integer value for a FancyNumber
// and 0 if any other FancyNumberBox is supplied.
func ExtractFancyNumber(fnb FancyNumberBox) int {
	fancyNumber, ok := fnb.(FancyNumber)
    answer := 0

    if ok {
        answer, _ = strconv.Atoi(fancyNumber.Value())
    }
    return answer
}

// DescribeFancyNumberBox should return a string describing the FancyNumberBox.
func DescribeFancyNumberBox(fnb FancyNumberBox) string {
	answer := ""
    switch value := fnb.(type) {
        case FancyNumber:
        	intValue, _ := strconv.Atoi(value.Value())
        	answer = fmt.Sprintf("This is a fancy box containing the number %.1f", float64(intValue))
        default:
        	answer = fmt.Sprintf("This is a fancy box containing the number %.1f", float64(0))
    }

    return answer
}

// DescribeAnything should return a string describing whatever it contains.
func DescribeAnything(i interface{}) string {
	answer := ""

    switch value := i.(type) {
        case int:
        	answer = DescribeNumber(float64(value))
        case float64:
        	answer = DescribeNumber(value)
        case NumberBox:
        	answer = DescribeNumberBox(value)
        case FancyNumberBox:
        	answer = DescribeFancyNumberBox(value)
        default:
        	answer = "Return to sender"
    }

    return answer
}
