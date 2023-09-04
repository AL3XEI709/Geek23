import Data.ByteString (ByteString)
import qualified Data.ByteString as BS
import Data.Word
import qualified Data.ByteString.Char8 as C8

stringToBytes :: String -> C8.ByteString
stringToBytes = C8.pack


-- 使用 big-endian 字节顺序
bytesToIntBigEndian :: ByteString -> Integer
bytesToIntBigEndian bs = go 0 (reverse $ BS.unpack bs) 0
  where
    go :: Integer -> [Word8] -> Int -> Integer
    go acc [] _ = acc
    go acc (x:xs) shift = go (acc + (fromIntegral x * (256 ^ shift))) xs (shift + 1)



main :: IO ()
main = do
    let str = "Hello, Haskell!"

        bytes = stringToBytes str
        intValue = bytesToIntBigEndian bytes
    putStrLn $ "Integer value (big-endian): " ++ show intValue