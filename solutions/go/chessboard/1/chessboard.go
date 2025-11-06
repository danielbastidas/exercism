package chessboard

// Declare a type named File which stores if a square is occupied by a piece - this will be a slice of bools
type File []bool

// Declare a type named Chessboard which contains a map of eight Files, accessed with keys from "A" to "H"
type Chessboard map[string]File 

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file.
func CountInFile(cb Chessboard, file string) int {
	fileValue, exists := cb[file]
    count := 0

    if exists {
        for _, occupied  := range fileValue {
            if occupied {
                count += 1
            }
        }
    }

    return count
}

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank.
func CountInRank(cb Chessboard, rank int) int {
	count := 0

    if rank >= 1 && rank <= 8 {
    	for _, fileValue := range cb {
            for i, occupied := range fileValue {
                if (i+1) == rank && occupied {
                    count +=1
                }
            } 
        }    
    }

    return count
}

// CountAll should count how many squares are present in the chessboard.
func CountAll(cb Chessboard) int {
	count := 0

    for _, fileValue := range cb {
        for _,_ = range fileValue {
            count += 1
        }
    }
    
    return count
}

// CountOccupied returns how many squares are occupied in the chessboard.
func CountOccupied(cb Chessboard) int {
	count := 0

    for _, fileValue := range cb {
        for _, occupied := range fileValue {
            if occupied {
             	count += 1   
            }
        }
    }
    
    return count
}
