// -*- coding:utf-8-unix -*-

use proconio::input;
use proconio::marker::{Chars};

fn main() {
    input! {
        s: Chars,
    }
    let s_slice = s.as_slice();
    println!("{}{}{}",{s_slice[1]},{s_slice[2]},{s_slice[0]});
}
