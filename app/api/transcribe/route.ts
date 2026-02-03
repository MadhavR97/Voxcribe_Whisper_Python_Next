import { NextResponse } from "next/server"
import type { NextRequest } from "next/server"

export async function POST(req: Request) {
  try {
    const formData = await req.formData()
    const file = formData.get("file") as File

    if (!file) {
      return NextResponse.json(
        { error: "No file uploaded" },
        { status: 400 }
      )
    }

    // Forward file to Whisper backend
    const whisperForm = new FormData()
    whisperForm.append("file", file)

    const BACKEND_URL = process.env.BACKEND_URL || "http://localhost:8000"
    const whisperResponse = await fetch(
      `${BACKEND_URL}/transcribe`,
      {
        method: "POST",
        body: whisperForm,
      }
    )

    if (!whisperResponse.ok) {
      const errorText = await whisperResponse.text()
      console.error("Whisper backend error:", errorText)

      return NextResponse.json(
        { error: "Whisper transcription failed" },
        { status: 500 }
      )
    }

    const data = await whisperResponse.json()

    /**
     * Expected Whisper response shape:
     * {
     *   text: string,
     *   words: [{ word, start, end }]
     * }
     */

    if (!data?.text || typeof data.text !== "string") {
      return NextResponse.json(
        { error: "Empty transcription result" },
        { status: 500 }
      )
    }

    // Clean transcript (extra safety)
    const cleanedTranscript = data.text
      .replace(/\s+/g, " ")
      .trim()

    return NextResponse.json({
      transcript: cleanedTranscript,
      words: data.words ?? [],
    })

  } catch (error) {
    console.error("Transcription route error:", error)
    return NextResponse.json(
      { error: "Transcription failed" },
      { status: 500 }
    )
  }
}
