import Data.Char (isSpace)

-- Author: Sunil Shah
-- Description: HW6 of CSCI 6221
-- Date: 2024/10/13 
-- Version: 1.0

data NestedList a = Elem a | List [NestedList a] deriving (Show, Eq)

-- Custom reverse function
reverseList :: [a] -> [a]
reverseList = foldl (flip (:)) []

-- Function to reverse a nested list
reverseNestedList :: NestedList a -> NestedList a
reverseNestedList (Elem x) = Elem x
reverseNestedList (List xs) = List (reverseList (map reverseNestedList xs))

-- Function to parse a string into a nested list
parseNestedList :: String -> NestedList String
parseNestedList s = fst (parse s)
  where
    parse ('(':xs) = let (list, rest) = parseList xs in (List list, rest)
    parse xs = let (elem, rest) = break (\c -> isSpace c || c == '(' || c == ')') xs
               in (Elem elem, dropWhile isSpace rest)
    
    parseList (')':xs) = ([], xs)
    parseList xs = let (item, rest) = parse xs
                       (items, rest') = parseList (dropWhile isSpace rest)
                   in (item:items, rest')

-- Function to convert a nested list back to a string
nestedListToString :: NestedList String -> String
nestedListToString (Elem x) = x
nestedListToString (List xs) = "(" ++ unwords (map nestedListToString xs) ++ ")"

-- Main function to take user input and print the reversed nested list
main :: IO ()
main = do
  putStrLn "Enter a nested list of elements:"
  input <- getLine
  let nestedList = parseNestedList input
  let reversedNestedList = reverseNestedList nestedList
  putStrLn "Reversed nested list:"
  putStrLn (nestedListToString reversedNestedList)