package hamming

import "errors"

func Distance(a, b string) (int, error) {

    if len(a) != len(b) {
    	return 0, errors.New("")    
    }

    diffCount := 0
    for index, _ := range a {
        if a[index] != b[index] {
            diffCount += 1
        }
    }

    return diffCount, nil
    
}
