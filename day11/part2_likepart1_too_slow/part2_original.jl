using Printf

function split_integer(val::Int, digits::Int)
    half_length = div(digits, 2)
    divisor = 10^half_length
    val1 = div(val, divisor)
    val2 = mod(val, divisor)
    return val1, val2
end

function blink!(stones::Vector{Int})
    ind = 1
    while ind <= length(stones)
        val = stones[ind]
        if val == 0
            stones[ind] = 1
            ind += 1
            continue
        end
        digits = floor(Int, log10(val)) + 1
        if iseven(digits)
            val1, val2 = split_integer(val, digits)
            stones[ind] = val1
            insert!(stones, ind + 1, val2)
            ind += 2
        else
            stones[ind] = val * 2024
            ind += 1
        end
    end
end

function main(input::String, count::Int)
    datafile = joinpath("day11", input)
    stones = parse.(Int, split(strip(read(datafile, String)), " "))
    println(stones)
    for n in 1:count
        println("Blinked $n times")
        blink!(stones)
    end
    return length(stones)
end

test_result = main("test.txt", 25)
expected = 55312
if test_result != expected
    println("test failed $test_result != $expected")
else
    println(main("input.txt", 75))
end
