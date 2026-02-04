#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
mod ai_bridge;
use ai_bridge::AiBridge;
use serde_json::json;
#[tokio::main]
async fn main() {
    let mut ai = AiBridge::start().await;
    ai.send(json!({
        "type": "prompt",
        "id": "1",
        "text": "Explain ls -la"
    })).await;
    loop {
        tokio::time::sleep(std::time::Duration::from_secs(1)).await;
    }
