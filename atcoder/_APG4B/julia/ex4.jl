function year_to_seconds(n)
    seconds = 365*24*60*60
    return n*seconds
end

for n in [1 2 5 10]
    println(year_to_seconds(n))
end
