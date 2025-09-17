flowchart TB
  %% Layout and styles
  classDef math fill:#eaf2ff,stroke:#7aa2ff,stroke-width:1px,color:#1a2a3a;
  classDef sym  fill:#eaffe8,stroke:#7acc7a,stroke-width:1px,color:#1a3a2a;
  classDef note fill:#fff8e6,stroke:#c7a45a,stroke-dasharray:4 3,color:#4a3a1a;

  %% Arithmetic track
  subgraph A["Arithmetic Steps"]
    A0["144000 (12 × 12000)"]:::math
    A1["Subtract 144 (1/1000) → 143856"]:::math
    A2["÷ 6 → 23976  (short of 24000 by 24)"]:::math
    A3["÷ 6 → 3996   (short of 4000 by 4)"]:::math
    A4["÷ 6 → 666"]:::math
    A0 --> A1 --> A2 --> A3 --> A4
  end

  %% Symbolic track
  subgraph S["Symbolic Meaning"]
    S0["Perfection in fullness"]:::sym
    S1["Marked deficiency (Eccl 1:15; 2 Pet 3:8)"]:::sym
    S2["Measured by human imperfection (six)"]:::sym
    S3["Intensified imperfection (threefold)"]:::sym
    S4["Absolute imperfection"]:::sym
    S0 --> S1 --> S2 --> S3 --> S4
  end

  %% Mapping between tracks
  A0 --- S0
  A1 --- S1
  A2 --- S2
  A3 --- S3
  A4 --- S4

  %% Identity tying method and result
  I["Identity:\n(144000 − 144) / 6³ = 666\nand 666 × 216 + 144 = 144000"]:::note
  A4 --> I
  S4 --> I

  %% References (optional note)
  R["Refs: Rev 13:18; Rev 7:4; Rev 14:1; Eccl 1:15; 2 Pet 3:8"]:::note
  I --- R
