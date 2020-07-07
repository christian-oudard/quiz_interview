import Data.List (intercalate)

main = putStrLn $ format $ floyd 5
  where
    format rows = intercalate "\n" $ [ intercalate " " $ map show $ row | row <- rows ]

floyd numRows = take numRows $ loop [1..] 1
  where
    loop xs rowLen = row : (loop rest (rowLen + 1))
      where (row, rest) = splitAt rowLen xs
