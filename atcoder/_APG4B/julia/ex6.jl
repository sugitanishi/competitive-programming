function solve(a,op,b)
    if op=="+"
        a+b
    elseif op=="-"
        a-b
    elseif op=="/"
        b!=0 ? a÷b : "error"
    elseif op=="*"
        a*b
    else
        "error"
    end
end

a,op,b=split(readline())
a=parse(Int64,a)
b=parse(Int64,b)
println(solve(a,op,b))
