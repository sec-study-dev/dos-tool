use solana_program::{
    account_info::AccountInfo, entrypoint, entrypoint::ProgramResult, hash, msg, pubkey::Pubkey,
};
use std::str::from_utf8;

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let payload = String::from(from_utf8(instruction_data).unwrap())
        .parse::<i32>()
        .unwrap();
    let code: Vec<u8> = vec![255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255];
    for i in 1..payload {
        let hashcode = hash::hash(&code);
    }
    let log = format!("exhasust CPU {} times complete",payload);
    msg!(&log);
    Ok(())
}
