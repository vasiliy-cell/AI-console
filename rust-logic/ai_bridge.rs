use tokio::process::{Child, Command};
use tokio::io::{AsyncBufReadExt, AsyncWriteExt, BufReader};
use std::process::Stdio;
use serde_json::Value;

pub struct AiBridge {
    child: Child,
}

impl AiBridge {
    pub async fn start() -> Self {
        let mut child = Command::new("python3")
            .arg("-m")
            .arg("python.ai_service")
            .stdin(Stdio::piped())
            .stdout(Stdio::piped())
            .spawn()
            .expect("Failed to start python ai_service");

        let stdout = child.stdout.take().expect("No stdout");
        let mut reader = BufReader::new(stdout).lines();

        tokio::spawn(async move {
            while let Ok(Some(line)) = reader.next_line().await {
                match serde_json::from_str::<Value>(&line) {
                    Ok(msg) => {
                        println!("AI → {:?}", msg);
                    }
                    Err(e) => {
                        eprintln!("Invalid JSON from AI: {e}");
                    }
                }
            }
        });

        Self { child }
    }

    pub async fn send(&mut self, msg: Value) {
        let stdin = self.child.stdin.as_mut().expect("No stdin");
        let text = msg.to_string();
        stdin.write_all(text.as_bytes()).await.unwrap();
        stdin.write_all(b"\n").await.unwrap();
        stdin.flush().await.unwrap();
    }
}
