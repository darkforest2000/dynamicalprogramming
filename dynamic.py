package main

import (
	"fmt"
)

func main() {
	treasures := make(map[string][2]int, 0)
	treasures["Слиток"] = [2]int{5, 5000}
	treasures["Кубок"] = [2]int{3, 2000}
	treasures["Аркана на пуджа"] = [2]int{2, 1000}
	treasures["Самоцвет"] = [2]int{1, 1800}
	fmt.Println(bagPacking(treasures, 7))
}

func createCell(treasures map[string][2]int, capacity int) (cell [][]int, cellWithNames [][]string) {
	littleCell := make([]int, 0)
	littleCellWithNames := make([]string, 0)
	for range treasures {
		for i := 0; i < capacity; i += 1 {
			price := 0
			name := ""
			littleCell = append(littleCell, price)
			littleCellWithNames = append(littleCellWithNames, name)
		}
		cell = append(cell, littleCell)
		cellWithNames = append(cellWithNames, littleCellWithNames)
		littleCellWithNames = make([]string, 0)
		littleCell = make([]int, 0)
	}
	return cell, cellWithNames

}

func fillBackpack(Cell [][]int, treasures map[string][2]int, Names [][]string) [][]string {
	i := 0
	//! mapLog := make(map[int][]string)
	//! pLog := make([]string, len(Cell))
	for name, val := range treasures {
		// fmt.Println(name)
		for j := 1; j < len(Cell[i])+1; j++ {
			weight := val[0]
			price := val[1]
			currentSize := j
			if weight <= currentSize {
				price = val[1]
				if i != 0 {
					last_maximum, posiblePrice, nameOfPosible := Cell[i-1][j-1], price, name
					if currentSize > weight {
						nameOfPosible = name + " " + Names[i-1][j-1-weight]
						posiblePrice = price + Cell[i-1][j-1-weight]
					}
					if last_maximum > posiblePrice {
						Names[i][j-1] += Names[i-1][j-1]
						Cell[i][j-1] = last_maximum
					} else {
						Names[i][j-1] += nameOfPosible
						Cell[i][j-1] = posiblePrice
					}

				} else {
					Names[i][j-1] += name
					Cell[i][j-1] = price
				}
			} else if i != 0 {
				Names[i][j-1] += Names[i-1][j-1]
				Cell[i][j-1] = Cell[i-1][j-1]
			}
		}
		i++
	}
	return Names
}

func bagPacking(treasures map[string][2]int, capacity int) (backpack string) {
	emptyBag, emptyNames := createCell(treasures, capacity)
	cellWithNames := fillBackpack(emptyBag, treasures, emptyNames)
	LastLine := cellWithNames[len(cellWithNames)-1]
	return LastLine[len(LastLine)-1]
}
