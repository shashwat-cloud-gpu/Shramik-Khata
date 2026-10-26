# श्रमिक-खाता (Shramik-Khata)
### *The Autonomous Voice & Paper Wage Defense Ledger for Bharat's 450 Million Unorganized Workers*
**Built for the Sarvam AI Hackathon**

---

## 🏛️ The Problem (Seen from the Shoes of the Ground Labor Officer)
In India, over **450 million construction laborers, masons, painters, domestic workers, and artisans** work on unwritten verbal contracts.
- The contractor (*Thekedar*) maintains a single pocket diary scribbled in pencil (*Kaccha Khata*).
- The worker speaks their daily attendance, overtime, and advances in regional dialects (Bhojpuri, Maithili, Tamil, Telugu, Bundelkhandi) but has **no written record**.
- At the end of the month, the contractor marks false absent days, ignores overtime hours, inflates cash advances, and withholds 20% to 40% of the worker's earnings.
- When the worker appeals to the labor office or police, they are asked: *"कागज़ कहां है? (Where is the paper proof?)"*

**Shramik-Khata is an equalizer:** it gives the poorest worker the statutory auditing and legal defense power of an experienced Sub-Divisional Magistrate / Labor Enforcement Officer directly through their phone.

---

## ⚡ The Full 4-Engine Sarvam AI Stack

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               SARVAM MULTIMODAL PIPELINE                               │
├──────────────────────┬──────────────────────┬──────────────────────────────────────────┤
│ Sarvam Engine        │ Model ID             │ Ground Officer Function in Shramik-Khata │
├──────────────────────┼──────────────────────┼──────────────────────────────────────────┤
│ 1. Speech-to-Text    │ saaras:v4            │ Transcribes noisy, code-mixed, emotional │
│    (ASR)             │                      │ spoken voice notes in Indian dialects.   │
├──────────────────────┼──────────────────────┼──────────────────────────────────────────┤
│ 2. Document Vision   │ doc_ai (Digitise)    │ Scans crumpled, pencil-scrawled diaries  │
│    (OCR & Layout)    │                      │ and cash slips into structured tables.   │
├──────────────────────┼──────────────────────┼──────────────────────────────────────────┤
│ 3. Cognitive Brain   │ sarvam-105b-         │ Reconciles voice logs against the diary, │
│    & Legal Reasoner  │ conversations        │ detects wage theft, and cites statutory  │
│                      │                      │ clauses (Code on Wages, 2019).           │
├──────────────────────┼──────────────────────┼──────────────────────────────────────────┤
│ 4. Text-to-Speech    │ bulbul:v3            │ Speaks empathetic, authoritative ruling  │
│    (TTS)             │                      │ in natural Hindi/regional language voice.│
└──────────────────────┴──────────────────────┴──────────────────────────────────────────┘
```

---

## 🚀 Live Demo & How to Run

The server is currently running locally on:
```
https://shramikkhata.vercel.app/
```
---

## 🎯 3-Minute Hackathon Presentation Flow

1. **Minute 1: The Voice Log (Saaras v4)**
   - Click the big red microphone button and speak in Hindi/Bhojpuri:
     > *"ठेकेदार जी, आज मैंने सेक्टर 62 वाली साइट पर पूरा दिन काम किया और 2 घंटे ओवरटाइम किया।"*
   - Watch **Saaras v4** transcribe it live, and **Sarvam-105B** parse it into date, hours, overtime, and advances.

2. **Minute 2: The Contractor's Paper Diary (Sarvam Vision)**
   - View the uploaded photo of the Thekedar's messy pencil notebook where he secretly marked the worker "Absent" and omitted overtime.
   - Click **"डायरी स्कैन करें"** to run **Sarvam Vision (Doc AI)** to extract the tabular attendance.

3. **Minute 3: Ground Officer Audit & Ruling (Sarvam-105B + Bulbul v3)**
   - Click **"ऑडिट चलाएं"**:
     - Instantly flags **₹2,112.50 in wage theft**.
     - Cites **Code on Wages, 2019: Section 14 (2x Overtime Rate)** and **Section 18 (Illegal Deductions)**.
     - Click **"आवाज़ सुनें"** to hear **Bulbul v3** speak the advisory with warmth and clarity.
   - Click **"आधिकारिक वेतन पर्चा देखें"** to view and print the official, auditable Wage Slip ready for WhatsApp or the District Labor Officer.

---

## 📜 Statutory Legal Grounding
- **Section 13, Code on Wages 2019**: Fixation of hours of work for normal working day (8 hours).
- **Section 14, Code on Wages 2019**: Wages for overtime work at not less than twice the normal rate of wages.
- **Section 18, Code on Wages 2019**: Prohibition of unauthorized deductions and falsification of attendance records.
- **Section 54, Code on Wages 2019**: Powers of Inspectors-cum-Facilitators to inspect and summon employer records.
