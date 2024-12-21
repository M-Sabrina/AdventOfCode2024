function rotate_right(direction::Char)
    if direction == '>'
        return 'v'
    elseif direction == '<'
        return '^'
    elseif direction == 'v'
        return '<'
    elseif direction == '^'
        return '>'
    end
end

function forbidden(row::Int, col::Int, map::Array{Char, 2})
    symbol = map[row, col]
    forbidden_symbols = ['#', 'v', '^', '>', '<']
    return symbol in forbidden_symbols
end

function check_for_loops(row::Int, col::Int, map::Array{Char, 2})
    (max_row, max_col) = size(map)
    new_map = deepcopy(map)
    new_map[row, col] = '#'
    path_map = deepcopy(new_map)

    direction = nothing
    for symbol in ['<', '>', '^', 'v']
        if any(x -> x == symbol, new_map)
            idx = findfirst(==(symbol), new_map)
            (row, col) = Tuple(idx)
            direction = symbol
            break
        end
    end

    while true
        if direction == '>'
            new_row = row
            new_col = col + 1
        elseif direction == '<'
            new_row = row
            new_col = col - 1
        elseif direction == 'v'
            new_row = row + 1
            new_col = col
        elseif direction == '^'
            new_row = row - 1
            new_col = col
        end
        # println()
        # show(stdout, "text/plain", path_map)
        # sleep(0.2)

        # guard leaves map -> no loop
        if new_row < 1 || new_row > max_row || new_col < 1 || new_col > max_col
            return false
        # guard has walked here before -> loop
        elseif path_map[new_row, new_col] == direction
            return true
        # guard encounters obstacle -> turns right
        elseif new_map[new_row, new_col] == '#'
            direction = rotate_right(direction)
            new_map[row, col] = direction
            if path_map[row, col] == direction
                return true
            end
        # guard walks straight
        else
            new_map[row, col] = '.'
            path_map[row, col] = direction
            new_map[new_row, new_col] = direction
            (row, col) = (new_row, new_col)
        end
    end
end

function main(input::String)
    datafile = joinpath("day06", input)
    lines = readlines(datafile)
    max_row = length(lines)
    max_col = length(lines[1])
    map = fill('.', max_row, max_col)
    for i in 1:max_row
        for j in 1:max_col
            map[i, j] = lines[i][j]
        end
    end
    output = 0
    for row in 1:max_row
        for col in 1:max_col
            if !forbidden(row, col, map)
                contains_loop = check_for_loops(row, col, map)
                if contains_loop
                    output += 1
                end
            end
        end
    end
    return output
end

function test()
    result = main("test.txt")
    expected = 6
    @assert result == expected "test failed $result != $expected"
end

if abspath(PROGRAM_FILE) == @__FILE__
    test()
    result = main("input.txt")
    println(result)
end
