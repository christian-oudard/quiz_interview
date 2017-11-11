-- https://code.google.com/codejam/contest/351101/dashboard#s=p1

main = do
  putStrLn $ reverseWords "test a is this"

longText n = unwords $ map (:[]) $ take n $ cycle ['a'..'z'] 

reverseWords :: String -> String
reverseWords = unwords . reverse . words
