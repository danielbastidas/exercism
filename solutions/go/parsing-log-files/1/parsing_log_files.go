package parsinglogfiles
import "regexp"

func IsValidLine(text string) bool {
	re := regexp.MustCompile(`^(\[TRC\]|\[DBG\]|\[INF\]|\[WRN\]|\[ERR\]|\[FTL\])+.*`)
    return re.MatchString(text)
}

func SplitLogLine(text string) []string {
	re := regexp.MustCompile(`<(~|\*|=|-)*>`)
    return re.Split(text, -1)
}

func CountQuotedPasswords(lines []string) int {
	count := 0
    re := regexp.MustCompile(`.*".*(?i)password.*".*`)

    for _, line := range(lines) {
        if re.MatchString(line) {
        	count += 1    
        }
    }
    
    return count
}

func RemoveEndOfLineText(text string) string {
	re := regexp.MustCompile(`end-of-line[0-9]+`)

    return re.ReplaceAllString(text, "")
}

func TagWithUserName(lines []string) []string {
    re := regexp.MustCompile(`User\s+(\w+)`)

    for index, _ := range(lines) {
    	matches := re.FindStringSubmatch(lines[index])
		
        if matches != nil {
            lines[index] = "[USR] " + matches[1] + " " + lines[index]
        }
    }

    return lines
    
}
