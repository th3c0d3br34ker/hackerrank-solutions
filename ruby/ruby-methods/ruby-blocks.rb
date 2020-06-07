def factorial
    yield
end

n = gets.to_i
factorial{
    puts (1..n).inject(:*)
}


