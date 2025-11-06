package twofer

func ShareWith(name string) string {
	dialogue := ""

    if name == "" {
        dialogue = "One for you, one for me."
    } else {
        dialogue = "One for " + name + ", one for me."
    }
    
	return dialogue
}
