getInts = do
    x <- getLine
    let y = map (read::String->Integer) (words x) 
    return y

main::IO()
main=do
    [a,b] <- getInts
    let (x,y) = ((a+11)`mod`13,(b+11)`mod`13)
    putStrLn$if x==y then "Draw" else if x>y then "Alice" else "Bob"
