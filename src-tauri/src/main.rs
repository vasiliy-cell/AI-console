// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
fn main() {
  app_lib::run();
}



use std::process::Command;


fn ai_service_run() {
    let status = Command::new("python3") 
        .arg("../../python/ai_service.py")
        .arg("-c")
        .output()
        .status()
        .expect("Не удалось запустить процесс");

     if output.status.success() {
        let result = String::from_utf8_lossy(&output.stdout);
        println!("Вывод Python: {}", result);
    } else {
        let error = String::from_utf8_lossy(&output.stderr);
        eprintln!("Ошибка: {}", error);
    }

}