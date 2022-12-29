fn main() {
    let d1 = include_str!("../data/d1.txt");
    let elves = d1.split("\n\n");
    let mut calories: Vec<i32> = elves
        .map(|serie| {
            let lines = serie.split("\n");
            lines.map(|l| str::parse::<i32>(l).unwrap()).sum::<i32>()
        })
        .collect::<Vec<i32>>();

    // calories.sort(); calories.reverse() is less generic
    calories.sort_by(|a, b| b.cmp(a));

    let p1: i32 = calories[0]; // .iter().max()
    let p2: i32 = calories.iter().take(3).sum();
    println!("{}", p1);
    println!("{}", p2);
}
