package collatzconjecture
import "errors"

func CollatzConjecture(n int) (int, error) {

    steps := 0
    var err error
    
    for n > 1 {
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
        steps++
    }

    if steps == 0 && n < 1 {
        err = errors.New("")
    } else {
        err = nil
    }

    return steps, err
}
