pprint(it...;sep=" ",ed="\n")=length(it)>0 ? (@inbounds for i in 1:length(it)-1;print(it[i],sep);end;print(last(it),ed)) : print(ed)

k,n=parse.(Int64, split(readline()))
a=parse.(Int64, split(readline()))
mx=0
for i in 1:n-1
    global mx
    mx=max(a[i+1]-a[i],mx)
end
mx=max(mx,(k-a[n])+a[1])
pprint(k-mx)
