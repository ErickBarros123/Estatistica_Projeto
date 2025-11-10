# Medidas de Tendência Central

print('Medidas de Tendência Central para o Dataset:')
print('\nMean (Média):')
display(df.mean(numeric_only=True))

print('\nMedian (Mediana):')
display(df.median(numeric_only=True))

print('\nMode (Moda - pode retornar múltiplos valores se houver empate):')

for column in df.select_dtypes(include=np.number).columns:
    modes = df[column].mode()
    if not modes.empty:
        print(f'{column}: {modes.iloc[0]}')
    else:
        print(f'{column}: N/A')




#omparação das Medidas de Tendência Central (Média, Mediana, Moda)

import matplotlib.pyplot as plt
import seaborn as sns

# Recalculando todas as modas 
modes_dict = {}
for column in df.select_dtypes(include=np.number).columns:
    modes = df[column].mode()
    if not modes.empty:
        modes_dict[column] = modes.iloc[0]
    else:
        modes_dict[column] = np.nan # Uso de NaN

mean_values = df.mean(numeric_only=True)
median_values = df.median(numeric_only=True)
mode_values = pd.Series(modes_dict, name='Mode')

# Combinando tudo em um único DataFrame para a Plotagem ficar simples
central_tendencies_df = pd.DataFrame({
    'Mean': mean_values,
    'Median': median_values,
    'Mode': mode_values
})

# Filtro de colunas, limpeza
central_tendencies_df = central_tendencies_df.dropna(how='all') # Removendo linhas com NaN

# Reorganização para gráfico de barras
central_tendencies_melted = central_tendencies_df.reset_index().rename(columns={'index': 'Feature'}) \
                                  .melt(id_vars='Feature', var_name='Measure', value_name='Value')

# Plotando as medidas de tendência Central em um gráfico de barras
plt.figure(figsize=(18, 8))
sns.barplot(x='Feature', y='Value', hue='Measure', data=central_tendencies_melted, palette='viridis')
plt.title('Comparação das Medidas de Tendência Central por Coluna Numérica')
plt.ylabel('Valor')
plt.xlabel('Coluna')
plt.xticks(rotation=90)
plt.legend(title='Medida')
plt.tight_layout()
plt.show()





# Análise visual das medidas de tendência central usando box plots


# Selecionar algumas colunas para box plots de 1 a 4
# Inclusão das colunas GRADE E COURSE ID.
selected_columns_for_boxplot = ['GRADE', 'COURSE ID', '1', '2', '3', '4']

plt.figure(figsize=(18, 12))

for i, col in enumerate(selected_columns_for_boxplot):
    plt.subplot(2, 3, i + 1) # Ajuste na grade do subplot conforme o número de colunas selecionadas
    sns.boxplot(y=df[col], palette='coolwarm')
    plt.title(f'Box Plot de {col}')
    plt.ylabel('') 

    # Média representa como um X vermelho
    mean_val = df[col].mean()
    plt.scatter(x=0, y=mean_val, color='red', marker='X', s=150, label=f'Média: {mean_val:.2f}', zorder=5)

    # Adicionar a moda como um ponto verde ('o')
    modes = df[col].mode()
    if not modes.empty and len(modes) == 1: # Apenas se houver uma única moda clara
        mode_val = modes.iloc[0]
        plt.scatter(x=0, y=mode_val, color='green', marker='o', s=150, label=f'Moda: {mode_val:.2f}', zorder=5)
    elif not modes.empty and len(modes) > 1:
        # Trabalhando com multiplas modas
        for m_val in modes:
            plt.scatter(x=0, y=m_val, color='green', marker='o', s=100, alpha=0.6, zorder=5) # Plotar todos as modas
        plt.text(0.1, plt.ylim()[1]*0.9, 'Múltiplas Modas', color='green', verticalalignment='top', fontsize=9)

    plt.legend(loc='best', fontsize=9)

plt.tight_layout()
plt.show()
