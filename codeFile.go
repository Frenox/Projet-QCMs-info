package main

import "fmt"

// Définit une fonction qui prend un entier en paramètre, le multiplie par 5, puis affiche le résultat
func test(a int) {
    b := 5
    fmt.Println(a * b)
}

func main() {
    test(5) // Appelle la fonction test avec 5 comme argument
    test(8) // Appelle la fonction test avec 8 comme argument
    test(3) // Appelle la fonction test avec 3 comme argument
}
