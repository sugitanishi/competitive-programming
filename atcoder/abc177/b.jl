function dist(a,b)
    ret = 0
    for i = 1:length(a)
        c, v = a[i], b[i]
        ret += c!=v ? 1 : 0
    end
    ret
end

a=readline()
b=readline()

sol=999999999
for i = 1:length(a)-length(b)+1
    global sol
    sa = a[i:i+length(b)-1]
    sol=min(dist(sa,b), sol)
end
println(sol)