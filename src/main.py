from multi_agent.pipeline import run_pipeline

if __name__ == "__main__":
    topic = "Impacto da inteligência artificial no mercado de trabalho"
    
    result = run_pipeline(topic)

    print("\n=== RESULTADO FINAL ===\n")
    print(result)
