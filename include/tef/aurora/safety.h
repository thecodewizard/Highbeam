#pragma once
#include "tef/aurora/effectRunner.h"
#include "tef/aurora/smartFuse.h"
#include "tef/aurora/effects/debugEffect.h"
#include "tef/aurora/properties.h"
#include <iostream>
#include <thread>
#include <chrono>
#include <spdlog/spdlog.h>

namespace TEF::Aurora {

	class Safety
	{
	public:
		Safety()
		{
			m_smartFuse.Connect();
			m_smartFuse.Run();
		};

		~Safety()
		{
			m_smartFuse.StopAll();
		};

		void BuildCurrentMatrix()
		{
			EffectRunner effectRunner;

			m_debugEffect = std::make_shared<Effects::DebugEffect>();
			effectRunner.AddEffect(m_debugEffect);

			effectRunner.Run();

			m_smartFuse.SetFet(7, true);

			float current;

			for (int r = 0; r < 10; r++)
			{
				for (int g = 0; g < 10; g++)
				{
					for (int b = 0; b < 10; b++)
					{
						m_debugEffect->r = r;
						m_debugEffect->g = g;
						m_debugEffect->b = b;

						std::this_thread::sleep_for(std::chrono::milliseconds(100));
						m_smartFuse.GetCurrent(7, current);
						m_currentMatrix.data[r][g][b] = current - 0.65;
						spdlog::debug("rgb: {} {} {}", r, g, b);
					}
				}
			}

			m_smartFuse.SetFet(7, false);

			effectRunner.Stop();

			Properties::SaveProperty(m_currentMatrix);

		};

		void PrintCurrentMatrix()
		{
			for (int r = 0; r < 10; r++) {
				for (int g = 0; g < 10; g++) {
					for (int b = 0; b < 10; b++) {
						std::cout << m_currentMatrix.data[r][g][b] << ",";
					}
					std::cout << std::endl;
				}
			}
		}

	private:
		std::shared_ptr<Effects::DebugEffect> m_debugEffect;
		TEF::Aurora::SmartFuse m_smartFuse;

		Properties::CurrentMatrix m_currentMatrix;
	};
};
