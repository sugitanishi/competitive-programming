parseInt(x)=parse(Int, x)
parseMap(x::Array{SubString{String},1})=map(parseInt, x)
pprint(it...;sep=" ",ed="\n")=length(it)>0 ? (@inbounds for i in 1:length(it)-1;print(it[i],sep);end;print(last(it),ed)) : print(ed)

n = readline() |> parseInt
a = readline() |> split |> parseMap
b = zeros(Int,n)
for i in 1:n-1
    b[a[i]]+=1
end
pprint(b...,sep='\n')

