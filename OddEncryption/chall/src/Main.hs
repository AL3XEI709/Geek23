import Data.ByteString (ByteString)
import qualified Data.ByteString as BS
import Data.Word
import Data.Bits
import qualified Data.ByteString.Char8 as C8

f1 :: String -> C8.ByteString
f1 = C8.pack

f2 :: ByteString -> Integer
f2 bs = go 0 (reverse $ BS.unpack bs) 0
  where
    go :: Integer -> [Word8] -> Int -> Integer
    go acc [] _ = acc
    go acc (x:xs) shift = go (acc + (fromIntegral x * (256 ^ shift))) xs (shift + 1)

f3 :: Integer -> Integer -> (Integer, Integer)
f3 r mask =
    let n = 340282366920938463463374607431768211455
        output = (r `shiftL` 1) .&. n
        i = (r .&. mask) .&. n
        lastBit = foldl1 xor $ map (\j -> (i `shiftR` j) .&. 1) [0..127]
    in (output `xor` lastBit, lastBit)

main :: IO ()
main = do
    let mask = 322121453779346992541359934248135444081
        numBits = 128
        flag = "Al3XEI_FAKE_FLAG" -- length of flag equals 16
        bytes = f1 flag
        initialState = f2 bytes
    let (_, resultBits) = foldl (\(r, res) _ ->
            let (r', out) = f3 r mask
            in (r', res ++ [out])
          ) (initialState, []) [1..numBits]
    putStrLn "Odd Encryption Output:"
    putStrLn $ concatMap show resultBits
